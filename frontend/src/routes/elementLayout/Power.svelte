<script lang="ts">
import Power from "../../assets/on.svg"

const urlApi :string = "http://127.0.0.1:8081"
const endpoint: string = "/power"
const json: string = "robot_power"

let validated:boolean = true;
let stateRobot:boolean = true;

async function postData(urlApi:string,endpoint:string, json:string){
        try{
            console.log("ok")
            const response = await fetch(`${urlApi}${endpoint}`, 
                {
                    method: "POST",
                    headers:{
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({[json]:stateRobot})
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

const handleOnOffRobot = () =>{
    if (stateRobot === true){
        stateRobot = false;
        postData(urlApi,endpoint,json)
    } 
    else{
        stateRobot = true
        postData(urlApi,endpoint,json)

    }
}



</script>
<style lang="scss">
    .Power{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: transparent;
        border: none;
        border-radius:5px;
        width:40px;
        height:90%;
        color:white;
        img{
            height:70%;
            width: 70%;
            filter: brightness(0) invert(1);

        }
        &:hover{
        border: solid 1px white;
        color: #0f0c29;
        background-color: #fff;
        }
        &:hover img{
            filter: none;
        }
    }

.statut_robot_on_off{
    background-color: greenyellow;
    height:20px;
    width: 20px;
    border-radius: 15px;
    margin-left: 5px;
    border:1px solid white;
}


@media(max-width:740px){
    .Power{
        width:33px;
        height:29px;
        display: flex;
        align-items: center;
        justify-content: center;
        img{
            height:26px;
            width: 26px;
        }
    }
    .statut_robot_on_off{
        height:20px;
        width: 20px;
        margin-right: 50px;
    }
    
}
</style>



<button class= "Power" on:click={handleOnOffRobot}><img src={Power} alt="Power"/></button>
<div class="statut_robot_on_off">

</div>