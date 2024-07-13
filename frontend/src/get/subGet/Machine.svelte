<script>
import { onMount, onDestroy } from "svelte";

const ENDPOINT = 'ws://127.0.0.1:8081/statemachine'; // Notez que '/porte' est omis ici

let stateMachine= false;
let socket;

onMount(()=>{
    if (window.WebSocket){
        socket = new WebSocket(ENDPOINT);
        socket.onopen = (event)=> {
            console.log('Connecté au serveur WebSocket');
        }
        socket.onmessage = (event) =>{
            const data = JSON.parse(event.data);
           stateMachine= data.state_machine;
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
    .machine {
        border: 1px solid #ccc;
        padding: 20px;
        color: rgb(40, 2, 40);
        margin: 10px;
        margin-top: 20px;
        width: 200px;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 8px;
    }

    .light_state_machine {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin: auto;
        margin-bottom: 10px;
    }
    .light_state_machine.verte {
        background-color: green;
    }

    .light_state_machine.rouge {
        background-color: red;
    }

</style>

<div class = "machine">
    <div class = "light_state_machine {stateMachine === 1 ? 'verte':'rouge'}"></div>
    {#if stateMachine}
    <span>En cours ...</span>
    {:else}
    <span>Pause</span>
    {/if}
</div>