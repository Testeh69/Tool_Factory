<script>
    import { onMount, onDestroy } from "svelte";
    
    const ENDPOINT = 'ws://127.0.0.1:8081/historique'; // Notez que '/porte' est omis ici
    
    let historique= 0;
    let socket;
    
    onMount(()=>{
        if (window.WebSocket){
            socket = new WebSocket(ENDPOINT);
            socket.onopen = (event)=> {
                console.log('Connecté au serveur WebSocket');
            }
            socket.onmessage = (event) =>{
                const data = JSON.parse(event.data);
                historique = data.historique;
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
        .historique {
            border: 1px solid #ccc;
            padding: 20px;
            margin: 10px;
            width: 200px;
            text-align: center;
            background-color: #f0f0f0;
            border-radius: 8px;
        }
    
      
    
    </style>
    
    <div class = "historique">
        <p>Etape du processus: {historique}</p>
    </div>