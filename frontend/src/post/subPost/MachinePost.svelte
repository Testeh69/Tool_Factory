<script>
    let machinePlay = false;

    async function toggleMachine() {
        machinePlay = !machinePlay;
        try {
            const response = await fetch("http://127.0.0.1:8081/statemachine", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ state_machine: machinePlay })
            });
            const result = await response.json();
            console.log("Response from server:", result);
        } catch (error) {
            console.error("Error sending POST request:", error);
        }
    }
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
        top: 2px; /* Ajustement pour centrer verticalement */
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
    <span>Programme Machine: </span>
    <div class="border">
        <button type="button" class="btn__toggle {machinePlay ? 'play' : 'pause'}" on:click={toggleMachine}>
            <p>{machinePlay ? 'Play' : 'Pause'}</p>
        </button>
    </div>
</div>
