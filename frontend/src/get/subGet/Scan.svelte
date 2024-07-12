<script>
    import { onMount, onDestroy } from "svelte";

    const ENDPOINT = 'ws://127.0.0.1:8081/scan'; // Notez que '/porte' est omis ici

    let scanStatus = false;
    let socket;

    onMount(()=>{
        if (window.WebSocket){
            socket = new WebSocket(ENDPOINT);
            socket.onopen = (event)=> {
                console.log('Connecté au serveur WebSocket');
            }
            socket.onmessage = (event) =>{
                const data = JSON.parse(event.data);
                scanStatus = data.scan_status;
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
    .scan {
        border: 1px solid #ccc;
        padding: 20px;
        margin: 10px;
        width: 200px;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 8px;
    }

    .light_state_scan {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin: auto;
        margin-bottom: 10px;
    }

    .light_state_scan.verte {
        background-color: green;
    }

    .light_state_scan.rouge {
        background-color: red;
    }
</style>

<div class="scan">
    <div class="light_state_scan {scanStatus === 1 ? 'verte' : 'rouge'}"></div>
    {#if scanStatus}
        <span>Loaded ! </span>
    {:else}
        <span>Nothing</span>
    {/if}
</div>
