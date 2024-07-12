<script>
    import Historique from "./subGet/Historique.svelte";
import Machine from "./subGet/Machine.svelte";
    import Porte from "./subGet/Porte.svelte";
    import Scan from "./subGet/Scan.svelte";
</script>

<style>
    .Supervision_left, .Supervision_right {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin-left: 20px;
        margin-top: 20px; 
    }

.Supervision{
    display: flex;
    flex-direction: row;
}

    .frame_one {
        display: flex;
        flex-direction: column;
        margin-right: 20px;
    }
.Screen{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
  
</style>
<div class= "Screen">
    <div class="Supervision">
        <div class="Supervision_left">
            <div class="frame_one">
                <Porte /> 
                <Machine /> 
                <Scan /> 
            </div>
            <div class="frame_two">
                <Historique />
            </div>
            <div class="frame_three">
            </div>
        </div>
        <div class="Supervision_right">
            <div class="frame_one">
               
            </div>
            <div class="frame_two">
              
            </div>
            <div class="frame_three">
            </div>
        </div>
    </div>
</div>