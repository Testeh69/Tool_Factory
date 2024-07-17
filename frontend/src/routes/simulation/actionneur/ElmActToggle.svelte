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
            console.log(jsonObs,json[jsonObs])
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
    background-color: brown;
    margin-top: 20px;
    height:50px;
    .toggle{
        padding-top: 5px;
        .btn__toggle{        
            border-radius: 20px;
            width:20px;
            height:20px;
        }
        .green{
                background-color: greenyellow;
            }
        .red{
                background-color: red;
            }
    }

}


  
</style>

<div class="element__actionneur__toggle">
    <span>{name}</span>
    <div class="toggle">
        <button class= "btn__toggle {toggle_state === 1 ? "green": "red"}" on:click = {handleChangeState}></button>
    </div>
</div>
