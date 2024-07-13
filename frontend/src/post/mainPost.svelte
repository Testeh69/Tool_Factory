<script>
    import MachinePost from "./subPost/MachinePost.svelte";
    import PortePost from "./subPost/PortePost.svelte";
    import ScanPost from "./subPost/ScanPost.svelte";
    import HistoriquePost from "./subPost/HistoriquePost.svelte";
  import TimePost from "./subPost/TimePost.svelte";
</script>

<style>

.window_controleur{
    background-color: rgb(84, 2, 84);
    box-shadow:  3px 2px hsla(305, 68%, 83%, 0.5);    
    height:80vh;
    margin: 30px;
    border-radius: 10px;
    border: solid 0.1px hsla(305, 68%, 83%, 0.5);
    padding: 40px;
}



</style>


<div class= "controle">
    <div class= "window_controleur">
        <h2><span class="title">CONTROLEUR</span></h2>
        <TimePost/>
        <MachinePost />
        <PortePost />
        <ScanPost />
        <HistoriquePost />
    </div>
 
</div>