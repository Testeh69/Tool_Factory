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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

    font-size: 9px;
    padding-top: 10px;
    padding-bottom: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 5px;
    background-color: #0f0c29;
            background: linear-gradient(#0f0c29,#302b63,#24243e);
    height:40%;
    width: 100%;
    border: solid 1px black;

    
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
            height:25px;
            width: 25px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            .light{
                background: linear-gradient(to bottom left,#e7e7e2,#e8f004);
                height:80%;
                width:80%;
                border-radius: 15px;
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


@media (max-width: 700px) {
    .element__obs{
        height:40px;
        width: 50px;
        font-size: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
        .column_title{
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .column_data{
            .border{
                .light{
                    border-radius: 15px;
                    width:15px;
                }
            }
            .actualité{
                font-size: 15px;
            }
    }
}}
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
