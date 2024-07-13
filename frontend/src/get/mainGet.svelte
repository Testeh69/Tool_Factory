<script>
    import Historique from "./subGet/Historique.svelte";
import Machine from "./subGet/Machine.svelte";
    import Porte from "./subGet/Porte.svelte";
    import Scan from "./subGet/Scan.svelte";
</script>

<style>
.window_observeur{
    background-color: rgb(84, 2, 84);
    box-shadow:  3px 2px hsla(305, 68%, 83%, 0.5);    
    height:80vh;
    margin: 30px;
    border-radius: 10px;
    border: solid 0.1px hsla(305, 68%, 83%, 0.5);
    padding: 40px;
}


.title_window{
    display: flex;
    align-items: center;
    justify-content: center;
}
.title{
    color:#ebe8ee
}

</style>
<div class= "Screen">
    <div class= "window_observeur">
        <div class="title_window">
        <h2><span class="title">OBSERVEUR</span></h2>
        </div>
        <Machine />
        <Porte />
        <Scan />
        <Historique />
    </div>
 
</div>