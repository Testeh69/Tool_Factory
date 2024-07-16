<script lang="ts">
import ElmObs from "./observeur/ElmObs.svelte";

const objObservateur : {
    listNameObs: Array<String>, 
    listNameEndpoint: Array<String>, 
    listNameJson: Array<String>} = {
    listNameObs: ["Programme",
                "Etat de la porte",
                "Numéro de l'étape",
                "Etat de la machine",
                "Temps de cycle",
                "nombre de pièces"
                ],
    listNameEndpoint:["/scan",
                "/porte",
                "/historique",
                "/statemachine",
                "/cycle",
                "/parts"
    ],
    listNameJson: ["scan_status",
                "Porte_Ouverte",
                "historique",
                "state_machine",
                "time_cycle",
                "number_parts"
    ]

}

</script>
<style lang="scss">

.observeur__section{
    margin-left: 100px;
    margin-top: 40px;
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
        flex-direction: row;
        width: 100%;
        height:100%;
        align-items: center;
        justify-content: space-evenly;
    }
}


</style>

<section class="observeur__section">
    <span class="title">Observeur</span>
    <div class="observeur">
        <div class = "colonne-1">
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
        </div>
        <div class = "colonne-2">
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
            <ElmObs name = {"lol"} endpoint = {"l"}/>   
        </div>
    </div>
</section>


