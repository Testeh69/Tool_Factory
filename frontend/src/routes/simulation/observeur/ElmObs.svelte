<script lang="ts">
    import { onMount, onDestroy } from 'svelte';

    export let name: string;
    export let endpoint: string;
    export let json: string;
    export let urlWebSocket: string;
    let socket: WebSocket | null = null; 
    let dataAPI: number ; 

    onMount(() => {
        if (window.WebSocket) {
            socket = new WebSocket(`${urlWebSocket}${endpoint}`);

            socket.onopen = (event) => {
                console.log("Connected to the WebSocket server");
            };

            socket.onmessage = (event) => {
                const message = JSON.parse(event.data);
                dataAPI = message[json]
    
            };

            socket.onerror = (error) => {
                console.error('WebSocket connection error:', error);
            };

            socket.onclose = (event) => {
                console.log('Disconnected from the WebSocket server');
            };
        } else {
            console.log('WebSockets are not supported in this browser.');
        }
    });

    onDestroy(() => {
        if (socket) {
            socket.close(); // Close WebSocket connection when component is unmounted
        }
    });
</script>

<style lang="scss">
    .element__obs {
    margin: 5px;
    padding: 10px;
    display: flex; 
    align-items: center; 
    flex-direction: row;
    .column_title{
        display: flex;
        flex-direction: column;
        background-color: yellow;
        margin-right: 20px;
    }
    .column_data{
        background-color: white;
        width: 30px;
        height:30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;

        .rouge{
            height:100%;
            width:100%;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: red;
        }

        .verte{
            background-color: greenyellow;
            height:100%;
            width:100%;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        }
    
}

  
</style>

<div class="element__obs">
    <div class="column_title">
    {#if name === "Programme"}
    <span class="name">{dataAPI ? "Plan Chargé":"Vide"}</span>
    {:else if name === "Porte"}
    <span class="name">{dataAPI ? "Porte Ouverte": "Porte Fermée"}</span>
    {:else if name ==="Machine"}
    <span class="name">{dataAPI? "Machine en cours" :"Machine en Pause"}</span>
    {:else}
    <span class="name">{name}</span>
    {/if}
    </div>
    <div class="column_data">
    {#if name !== "Temps de cycle" && name !== "nombre de pièces" && name !== "Numéro de l'étape"}
        <div class="light {dataAPI === 1 ? "verte":"rouge"}">
        </div>
    {:else}
        <div class="actualité">
            <span>{dataAPI}</span>
        </div>
    {/if}
    </div>
</div>
