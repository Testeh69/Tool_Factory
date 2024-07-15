<script>
    import { onMount } from "svelte";
    
    const ENDPOINT = 'ws://127.0.0.1:8081/parts'; // Notez que '/porte' est omis ici
    
    let number_parts= 0;
    let socket;
    
    onMount(()=>{
        if (window.WebSocket){
            socket = new WebSocket(ENDPOINT);
            socket.onopen = (event)=> {
                console.log('Connecté au serveur WebSocket');
            }
            socket.onmessage = (event) =>{
                const data = JSON.parse(event.data);
                number_parts = data.number_parts;
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
        .number_parts {
            border: 1px solid #ccc;
        color: rgb(40, 2, 40);
        padding: 20px;
        margin: 10px;
        margin-top: 40px;
        height: 82px;
        width: 200px;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        }
    
      
    
    </style>
    
    <div class = "number_parts">
        <p>Nombre de pièce dans la machine: {number_parts}</p>
    </div>