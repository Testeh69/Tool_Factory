<script lang="ts">
    import {onMount, onDestroy} from "svelte"
    export let name: string;
    export let endpoint: string;
    export let json: string;
    export let jsonObs:string;
    export let urlApi: string;
    let validated : boolean;
    let toggle_state: number;
    let interval : number;

    async function getData(urlApi:string, endpoint:string, jsonObs:string){
        try{
            const response = await fetch(`${urlApi}${endpoint}`);
            if (!response.ok){
                throw new Error(`Response STATUS? ${response.status}`);
            }
            const json = await response.json()
            toggle_state = json[jsonObs];
        }
        catch(error){
            if(error instanceof Error){
                console.error(error.message)
            }
            else{
                console.error("Unpexpected error", error)
            }
        }
    }

    async function postData(urlApi:string,endpoint:string, json:string){
        try{
            const response = await fetch(`${urlApi}${endpoint}`, 
                {
                    method: "POST",
                    headers:{
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({[json]:toggle_state})
                }
            )
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            validated = true;
        } catch (error) {
            console.error("Error sending POST request:", error);
            validated = false;
        }
    }

    function handleChangeState(){
        toggle_state  = toggle_state === 1 ? 0: 1 ;
        postData(urlApi,endpoint,json)
    }
    


    onMount(()=>{
        interval = setInterval(()=>getData(urlApi, endpoint, jsonObs), 1000)
    })

    onDestroy(()=>{
        clearInterval(interval)
    })
</script>

<style lang="scss">

.element__actionneur__toggle{
    font-size: 12px;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 20px;
    height:20%;
    span{
        text-align: center;
    }
    .toggle{
        border-radius: 15px;
        border:solid 1px black;
        margin-top: 7px;
        margin-bottom: 7px;
        width:60%;
        background-color: #0f0c29;
    background: linear-gradient(#0f0c29,#302b63,#24243e);
        .btn__toggle{ 
            position: relative;      
            border-radius: 20px;
            border: none;
            width:30px;
            height:30px;
            transition: left 0.3s;
            background-color: #D9AFD9;
            background-image: linear-gradient(120deg, #D9AFD9 0%, #97D9E1 100%);

        }
        .play{
            left:calc(100% - 30px);
            background: radial-gradient(circle,#66ff66,#009933);
        }
        .pause{
                left: 0;
                background: radial-gradient(circle,#ffcc66,#cc0000);
        }
    }
}

@media (max-width: 700px) {
    .element__actionneur__toggle{
    font-size:8px;
    height:20px;
    margin-top: 60px;
    margin-bottom: 60px;
    .toggle{
        height:20px;
        width:60px;
        .btn__toggle{
            height:20px;
            width:20px;
        }
        .play{
            left:calc(100% - 20px)
        }

    }
    
}

}


  
</style>

<div class="element__actionneur__toggle">
    <span>{name}</span>
    <div class="toggle">
        <button class= "btn__toggle {toggle_state === 1 ? "play": "pause"}" on:click = {handleChangeState}></button>
    </div>
</div>
