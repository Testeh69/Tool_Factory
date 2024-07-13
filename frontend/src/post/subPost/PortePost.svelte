<script>
    import {onMount, onDestroy} from "svelte";

    const url = "http://127.0.0.1:8081/porte"
    let porteOuverte = false;
    let interval


    async function fetchData() {
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        porteOuverte =  json.porte
        
    } catch (error) {
        console.error(error.message);

    }}


    async function togglePorte() {
        porteOuverte = !porteOuverte;
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ porte_ouverte: porteOuverte })
            });
            const result = await response.json();
            console.log("Response from server:", result);
        } 
        catch (error) {
            console.error("Error sending POST request:", error);
        }
    }
    onMount(()=>{
        interval = setInterval(fetchData, 1000)
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
        top:3px;
        border: solid 0.5px;
        border-radius: 30px;
        width: 50px;
        height: 50px;
        display:flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        position: absolute;
        transition: left 0.3s;
    }

    .btn__toggle.ouverte {
        background-color: green;
        left: calc(100% - 50px); 
    }

    .btn__toggle.fermee {
        background-color: red;
        left: 0; 
    }
</style>

<div class="element">
    <span>Porte: </span>
    <div class="border">
        <button type="button" class="btn__toggle {porteOuverte ? 'ouverte' : 'fermee'}" on:click={togglePorte}>
            <p>{porteOuverte ? 'O' : 'F'}</p>
        </button>
    </div>
</div>
