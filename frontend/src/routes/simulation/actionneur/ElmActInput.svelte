<script lang="ts">
    export let name: string;
    export let endpoint: string;
    export let json: string;
    export let urlApi: string;
    let value: number = 0; 
    let validated: boolean;

    async function postData(urlApi: string, endpoint: string, json: string, value: number) {
        try {
            const response = await fetch(`${urlApi}${endpoint}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ [json]: value })
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
                validated = false;
            }

            const result = await response.json();
            validated = true;
            console.log("POST request successful:", result);
        } catch (error) {
            console.error("Error sending POST request:", error);
            validated = false
        }
    }

    function sendValue(event: KeyboardEvent) {
    if (event.key === "Enter") {
        if (endpoint === "/historique") {
            if (value > 6 ) {
                value = 6;
            }
            else if (value < 0){
                value = 0;
            }
        }

        else if (endpoint === "/parts"){
            if (value > 4 ){
                value = 4
            }
            else if (value <0){
                value = 0
            }
        }

        else if (endpoint === "/cycle"){
            if (value> 1000){
                value = 40
            }
            else if (value <0){
                value = 4
            }
        }
        postData(urlApi, endpoint, json, value).catch(console.error);
    }
}
</script>

<style lang="scss">
    .element__actionneur__input {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
        font-weight: bold;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        text-align: center;
        flex-direction: column;
        margin-top: 34px;
        margin-bottom: 34px;
        height: 50px;
        .value_selection{
            margin-top: 10px;
            border-radius: 7px;
        input[type = number]{
            border: none;
            background-color: #0f0c29;
            background: linear-gradient(#0f0c29,#302b63,#24243e);
            height:21px;
            width: 80px;
            border-radius: 7px;
            text-align: center;
        }}
        .green {
        border: solid 2px;
        border-color: #66ff66;
    }

    .red {
        border: solid 2px;
        border-color: #cc0000;
    }
    }
</style>

<div class="element__actionneur__input">
    <span>{name}</span>
    <div class="value_selection {validated === null ? "": (validated ? "green":"red")}">
        {#if endpoint === "/historique"}
            <input type="number" id = {name} min="0" max="6" bind:value={value} required on:keydown={sendValue}>
        {:else if endpoint === "/parts"}
            <input type="number" id = {name} min="0" max="4" bind:value={value} required on:keydown={sendValue}>
        {:else if endpoint === "/cycle"}
            <input type="number" id = {name} min="0" max="40" bind:value={value} required on:keydown={sendValue}>
        {/if}
    </div>
</div>
