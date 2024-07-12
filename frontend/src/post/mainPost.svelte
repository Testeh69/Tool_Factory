<script>
  import MachinePost from "./subPost/MachinePost.svelte";
import PortePost from "./subPost/PortePost.svelte";
  import ScanPost from "./subPost/ScanPost.svelte";
</script>

<style>
.controle{
    margin-top: 30px;
    border: solid 0.5px;
    border-radius: 20px;
    height:400px;
    width:800px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.frame{
    top:0px;
    display: flex;
    flex-direction: row;
}
.frame_one{
    display: flex;
    flex-direction: column;
}
</style>


<div class= "controle">
    <span>Controle Panel </span>
    <div class= "frame">
        <div class="frame_one">
            <PortePost />
            <MachinePost />

        </div>
        <div class= "frame_two">
            <ScanPost />
        </div>
    </div>
</div>