<script lang="ts">
  import axios from 'axios';

  let code = `import sqlite3\n\ndef get_user(id):\n    conn = sqlite3.connect('users.db')\n    cursor = conn.cursor()\n    query = "SELECT * FROM users WHERE id = '%s'" % id\n    cursor.execute(query)\n    return cursor.fetchone()`;
  let filename = "database_helper.py";
  let scanResult: any = null;
  let loading = false;

  async function triggerScan() {
    loading = true;
    scanResult = null;
    try {
      // Step 1: Tell backend to scan
      const response = await axios.post('http://localhost:8000/scan', {
        filename: filename,
        code: code
      });
      
      // Step 2: Fetch the results for that scan ID
      const details = await axios.get(`http://localhost:8000/scans/${response.data.scan_id}`);
      scanResult = details.data;
    } catch (e) {
      console.error(e);
      alert("Error: " + (e.response?.data?.detail || "Check backend console."));
    } finally {
      loading = false;
    }
  }

  // The One-Click Apply Logic
  function applyPatch(newCode: string) {
    code = newCode;
    alert("Patch applied! Re-run scan to verify.");
  }
</script>

<main class="container">
  <div class="header">
    <h1>Code Analyzer</h1>
    <p>Autonomous Bug-Fixing Agent</p>
  </div>

  <div class="grid">
    <section class="editor-pane">
      <h3>File: <input type="text" bind:value={filename} /></h3>
      <textarea bind:value={code} rows="15"></textarea>
      <button class="scan-btn" on:click={triggerScan} disabled={loading}>
        {loading ? "AI is Analyzing..." : "Scan & Suggest Fix"}
      </button>
    </section>

    <section class="results-pane">
      <h3>Analysis Results</h3>
      {#if scanResult}
        {#each scanResult.vulnerabilities as vuln}
          <div class="vuln-card">
            <div class="vuln-header">
              <span class="severity {vuln.severity.toLowerCase()}">{vuln.severity}</span>
              <strong>{vuln.vuln_type}</strong>
            </div>
            <p>{vuln.description}</p>
            
            <div class="patch-box">
              <h4>Suggested Patch:</h4>
              <pre><code>{vuln.suggested_patch}</code></pre>
              <button class="apply-btn" on:click={() => applyPatch(vuln.suggested_patch)}>
                Apply Suggested Fix
              </button>
            </div>
          </div>
        {:else}
          <div class="no-vulns">✅ Clean! No issues found.</div>
        {/each}
      {:else}
        <p class="placeholder">Click "Scan" to begin autonomous analysis.</p>
      {/if}
    </section>
  </div>
</main>

<style>
  /* Add some basic styling to make it look like a pro dashboard */
  .container { max-width: 1200px; margin: 0 auto; padding: 20px; font-family: 'Inter', sans-serif; color: #b1aeae; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 20px; }
  textarea { width: 100%; background: #1a1a1a; color: #00ff00; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 14px; border: none; }
  .scan-btn { width: 100%; padding: 12px; background: #4f46e5; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 10px; }
  .vuln-card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 15px; margin-bottom: 15px; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
  .severity { padding: 2px 8px; border-radius: 4px; font-size: 11px; text-transform: uppercase; margin-right: 10px; color: white; }
  .high { background: #ef4444; }
  .patch-box { background: #f0fdf4; border: 1px solid #bbf7d0; padding: 10px; border-radius: 6px; margin-top: 10px; }
  pre { font-size: 12px; background: #f8fafc; padding: 10px; overflow-x: auto; }
  .apply-btn { background: #16a34a; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 13px; }
</style>