<script>
    import { onMount } from 'svelte';

    let inputValue = '0';
    let validated = null;

    async function postData() {
        try {
            const response = await fetch("http://127.0.0.1:8081/historique", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ step_program: inputValue })
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
            if (inputValue > 6){
                inputValue = 6
            }
            postData();
        }
    }
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
    <span>Etape du processus selectionné: </span>
    <input type="number" bind:value={inputValue} class={validated === null ? '' : (validated ? 'green' : 'red')} on:keydown={handleKeyDown} min=0 max=6 required>
</div>
