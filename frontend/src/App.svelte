<script>
	import MainGet from "./get/mainGet.svelte";
	import MainPost from "./post/mainPost.svelte";
</script>
<style>
.app{
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}
</style>
<main>
	<div class = "app">
	<MainGet />
	<MainPost />
	</div>
</main>

