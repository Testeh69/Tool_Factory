<script>
    import { onMount, onDestroy } from "svelte";

    const url = "http://127.0.0.1:8081/scan";
    let programLoaded = 1;
    let interval;

    async function fetchData() {
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        programLoaded =  json.scan
        
    } catch (error) {
        console.error(error.message);

    }}


    async function toggleMachine() {
    programLoaded = programLoaded === 1 ? 0 : 1; 
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ state_scan: programLoaded}),
      });
      const result = await response.json();
    } catch (error) {
      console.error("Error sending POST request:", error);
    }
  }
  

  onMount(() =>{
    interval = setInterval(fetchData,1000)
})

onDestroy(()=>{
    clearInterval(interval)
})

  
</script>

<style>
    .element {
        border: 1px solid #ccc;
        padding: 20px;
        margin: 10px;
        width: 200px;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 8px;
    }

    .border {
        display: flex;
        align-items: center;
        margin-top: 5px;
        border: solid 0.5px;
        height: 55px;
        border-radius: 30px;
        border-color: rgb(21, 21, 21);
        box-shadow: 1px 1px 1px;
        position: relative;
        width: 100%;
    }

    .btn__toggle {
        border: solid 0.5px;
        border-radius: 30px;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        position: absolute;
        transition: left 0.3s;
        top: 2px; 
    }

    .btn__toggle.play {
        background-color: green;
        left: calc(100% - 50px); 
    }

    .btn__toggle.pause {
        background-color: red;
        left: 0; 
    }
</style>
<div class="element">
    <span>Statut du Programme: <strong>{programLoaded === 1? 'Load' : 'Unload'}</strong></span>

    <div class="border">
        {#if programLoaded !== undefined}
        <button type="button" class="btn__toggle {programLoaded === 1 ? "play":"pause"}"   on:click={toggleMachine}>
        </button>
        {/if}
    </div> 
</div>
