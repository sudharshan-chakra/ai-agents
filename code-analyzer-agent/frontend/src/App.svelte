<script lang="ts">
  import axios from 'axios';

  let code = `def get_user(id):\n    query = "SELECT * FROM users WHERE id = '%s'" % id\n    return db.execute(query)`;
  let filename = "database_helper.py";
  let scanResult: any = null;
  let loading = false;

  async function triggerScan() {
    loading = true;
    try {
      const response = await axios.post('http://localhost:8000/scan', {
        filename,
        code
      });
      // Fetch the details immediately after scan
      const details = await axios.get(`http://localhost:8000/scans/${response.data.scan_id}`);
      scanResult = details.data;
    } catch (e) {
      alert("Error connecting to backend. Is uvicorn running?");
    } finally {
      loading = false;
    }
  }
</script>

<main class="container">
  <h1>ZeroPath Lite 🛡️</h1>
  <p>Autonomous Bug-Fixer Prototype</p>

  <div class="grid">
    <section>
      <h3>Paste Python Code</h3>
      <input type="text" bind:value={filename} placeholder="filename.py" />
      <textarea bind:value={code} rows="10"></textarea>
      <button on:click={triggerScan} disabled={loading}>
        {loading ? "Analyzing..." : "Scan & Fix"}
      </button>
    </section>

    <section>
      <h3>Triage & Results</h3>
      {#if scanResult}
        {#each scanResult.vulnerabilities as vuln}
          <div class="card">
            <span class="badge {vuln.severity.toLowerCase()}">{vuln.severity}</span>
            <h4>{vuln.vuln_type}</h4>
            <p>{vuln.description}</p>
            
            <div class="patch-container">
              <h5>Suggested Patch:</h5>
              <pre><code>{vuln.suggested_patch}</code></pre>
              <button class="apply-btn">One-Click Apply</button>
            </div>
          </div>
        {:else}
          <p class="success">✅ No vulnerabilities found!</p>
        {/each}
      {:else}
        <p>Run a scan to see autonomous patches.</p>
      {/if}
    </section>
  </div>
</main>

<style>
  .container { max-width: 1000px; margin: 0 auto; padding: 2rem; font-family: sans-serif; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
  textarea { width: 100%; font-family: monospace; background: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 8px; }
  .card { border: 1px solid #ddd; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; background: #f9f9f9; }
  .badge { padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }
  .high { background: #ff4d4d; color: white; }
  .patch-container { background: #e6fffa; padding: 1rem; border: 1px solid #38b2ac; border-radius: 4px; margin-top: 1rem; }
  pre { font-size: 0.85rem; overflow-x: auto; }
  .apply-btn { background: #38b2ac; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; }
</style>