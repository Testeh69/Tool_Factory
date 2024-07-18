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
   .element__obs{
    font-size: 9px;
    padding-top: 10px;
    padding-bottom: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 5px;
    background: rgb(0,22,250);
    background: linear-gradient(120deg, rgba(0,22,250,1) 0%, rgb(79, 94, 215) 50%, rgba(6,161,254,1) 75%);            
    height:40%;
    width: 100%;
    border: solid 1px black;
    box-shadow: 1px 1px 1px;
    
    .column_title{
        height:50%;
        display:flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;;
    }
    .column_data{
        height:50%;
        width:100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 3px;
        .actualité{
            font-size: 20px;
        }
        .border{
            background:linear-gradient(to bottom left,#222328,#a2a8ba);
            height:25px;
            width: 25px;
            box-shadow: 1px 1px 1px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            .light{
                background: linear-gradient(to bottom left,#e7e7e2,#e8f004);
                height:80%;
                width:80%;
                border-radius: 15px;
                border: solid 1px;
            }
            .rouge{
                background: radial-gradient(circle,#ffcc66,#cc0000);
            }
            .verte{
                background: radial-gradient(circle,#66ff66,#009933);
                
            }
            
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
    <span class="name">{dataAPI? "Machine en cours" :"Machine en pause"}</span>
    {:else}
    <span class="name">{name}</span>
    {/if}
    </div>
    <div class="column_data">
    {#if name !== "Temps de cycle" && name !== "Nombre de pièces" && name !== "Numéro de l'étape"}
        <div class="border">
            <div class="light {dataAPI === 1 ? "verte":"rouge"}">
            </div>
        </div>
    {:else}
        {#if name === "Temps de cycle"}
            <div class="actualité">
                <span>{dataAPI}s</span>
            </div>
        {:else}
            <div class="actualité">
                <span>{dataAPI}</span>
            </div>
        {/if}
    {/if}
    </div>
</div>
