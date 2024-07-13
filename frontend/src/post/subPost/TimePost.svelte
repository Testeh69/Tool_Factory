<script>
    import { onMount, onDestroy } from 'svelte';
    let url = "http://127.0.0.1:8081/cycle"
    let timeCycle = '0';
    let validated = null;
    let timeCycleGet;
    let interval;

    async function fetchData() {
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        timeCycleGet =  json.time_cycle
        
    } catch (error) {
        console.error(error.message);

    }}


    async function postData() {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ time_cycle: timeCycle })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            validated = true;
            console.log("Response from server:", result);
        } catch (error) {
            console.error("Error sending POST request:", error);
            validated = false;
        }
    }

    function handleKeyDown(event) {
        if (event.key === "Enter") {
            if (timeCycle > 60){
                timeCycle = 60
            }
            postData();
        }
    }


    onMount(()=>{
        interval = setInterval(fetchData, 500)
    })

    onDestroy(()=>{
        clearInterval(interval)
    })
</script>

<style>
    .element {
        border: 1px solid #ccc;
        color: rgb(40, 2, 40);
        padding: 20px;
        margin: 10px;
        margin-top: 40px;
        width: 200px;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
    }
    

    input[type="number"] {
        display: flex;
        text-align: center;
        font-size: 28px;
        margin-top: 20px;
        height:30px;
        border-radius: 10px;
    }

    .green {
        border: solid;
        border-color: rgb(62, 229, 62);
    }

    .red {
        border: solid;
        border-color: rgb(227, 37, 37);
    }
</style>

<div class="element">
    <span>Temps de Cycle {timeCycleGet} secondes: </span>
    <input type="number" bind:value={timeCycle} class={validated === null ? '' : (validated ? 'green' : 'red')} on:keydown={handleKeyDown} min=0 max=60 required>
</div>
