<script lang="ts">
import {writable} from "svelte/store";
import ElmObs from "./simulation/observeur/ElmObs.svelte";

const urlObject : {urlWebSocket:String, urlApi: String} = {
  urlWebSocket: "ws://127.0.0.1:8081",
  urlApi:"http://127.0.0.1:8001"
}

const urlStore = writable(urlObject)

</script>
  
  <style lang="scss">
  main {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
</style>
  
<main>
</main>
  