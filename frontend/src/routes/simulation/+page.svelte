<script lang="ts">
import ElmObs from "./observeur/ElmObs.svelte";
import ElmActToggle from "./actionneur/ElmActToggle.svelte";
import ElmActInput from "./actionneur/ElmActInput.svelte";

interface urlObject {
  urlWebSocket:string;
  urlApi:string;
}

const urlObject : urlObject = {
  urlWebSocket: "ws://127.0.0.1:8081",
  urlApi:"http://127.0.0.1:8001"
}


interface Actionneur{
    listNameAct: string[],
    listNameEndPoint: string[],
    listNameJson: string[]  
}

const objActionneurToggle: Actionneur = {
    listNameAct:[
                "Charger le programme",
                "Bouger la porte",
                "Affecter le programme",],
    listNameEndPoint:[
                "/scan",
                "/porte",
                "/statemachine"],
    listNameJson:[
            "scan_status",
            "Porte_Ouverte",
            "state_machine"
    ]
}

interface Observateur {
    listNameObs: string[],
    listNameEndPoint: string[],
    listNameJson: string[]       
} 


const objObservateur: Observateur = {
    listNameObs:["Programme",
                "Etat de la porte",
                "Etat de la machine",
                "Numéro de l'étape",
                "nombre de pièces"
                ],
    listNameEndPoint:["/scan",
                "/porte",
                "/statemachine",
                "/historique",
                "/parts"
    ],
    listNameJson: ["scan_status",
                "Porte_Ouverte",
                "state_machine",
                "historique",
                "number_parts"
    ]

}

</script>
<style lang="scss">


.section__virtualisation{
    display: flex;
    flex-direction: row;

.observeur__section{
    margin-left: 100px;
    margin-top: 10vh;
    background-color: yellow;
    height:80vh;
    width: 20vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    .title{
        display: flex;
        text-align: center;
        width: 100%;
        background-color: red;
        padding-top: 20px;
        align-items: center;
        justify-content: center;
    }
    .observeur{
        background-color: green;
        display: flex;
        flex-direction: column;
        width: 100%;
        height:100%;
        align-items: center;
        justify-content: space-evenly;
    }
}
.actionneur__section{
    margin-left: 100px;
    margin-top: 10vh;
    background-color: yellow;
    height:80vh;
    width: 20vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    .title{
        display: flex;
        text-align: center;
        width: 100%;
        background-color: red;
        padding-top: 20px;
        align-items: center;
        justify-content: center;
    }

}

}


</style>
<section class="section__virtualisation">
    <section class="observeur__section">
        <span class="title">Observeur</span>
        <div class="observeur">
            {#each objObservateur.listNameObs as obs, index}
                <ElmObs 
                    name = {obs} 
                    endpoint = {objObservateur.listNameEndPoint[index]} 
                    json = {objObservateur.listNameJson[index]} 
                    urlWebSocket = {urlObject.urlWebSocket}
                />
            {/each}
        </div>
    </section>
    <section class="actionneur__section">
        <span class="title">Actionneur</span>
        <div class="actionneur">
            <div class="actionneur__toggle">
                {#each objActionneurToggle.listNameAct as act, index}
                    <ElmActToggle
                    name = {act}
                    endpoint = {objActionneurToggle.listNameEndPoint[index]}
                    json = {objActionneurToggle.listNameJson[index]}
                    urlApi = {urlObject.urlApi}
                    />
                {/each}
            </div>
            <div class="actionneur__input">

            </div>
        </div>
    </section>
</section>


