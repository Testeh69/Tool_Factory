<script>
    import { onMount, onDestroy } from "svelte";

    const ENDPOINT = 'ws://127.0.0.1:8081/porte'; // Notez que '/porte' est omis ici

    let porteOuverte = false;
    let socket;

    onMount(()=>{
        if (window.WebSocket){
            socket = new WebSocket(ENDPOINT);
            socket.onopen = (event)=> {
                console.log('Connecté au serveur WebSocket');
            }
            socket.onmessage = (event) =>{
                const data = JSON.parse(event.data);
                porteOuverte = data.Porte_Ouverte;
            }
            socket.onerror = (error) => {
                console.error('Erreur de connexion WebSocket:', error);
            };

            socket.onclose = (event) => {
                console.log('Déconnecté du serveur WebSocket');
            };} 
        else {
            console.log('WebSockets ne sont pas supportés dans ce navigateur.');
        }
        
    })
   
</script>

<style>
    .porte {
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

    .light_state_porte {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin: auto;
        margin-bottom: 10px;
    }

    .light_state_porte.verte {
        background-color: green;
    }

    .light_state_porte.rouge {
        background-color: red;
    }
</style>

<div class="porte">
    <div class="light_state_porte {porteOuverte === 1 ? 'verte' : 'rouge'}"></div>
    {#if porteOuverte}
        <span>Porte ouverte</span>
    {:else}
        <span>Porte fermée</span>
    {/if}
</div>
