<script setup>
import { ref } from "vue";
import axios from "axios";

const emit = defineEmits(["sendOutput"]);

const inputText = ref("");
const exibirresposta = ref("");

async function prompt() {
  try {
    const response = await axios.post("http://localhost:3000/prompt", {
      inputText: inputText.value,
    });

    exibirresposta.value = response.data.response || "Sem Resposta";
    emit("sendOutput", { response: exibirresposta.value, success: true });
  } catch (error) {
    console.log("Erro ao enviar resposta:", error);
    exibirresposta.value = "Erro ao processar a resposta. Tente novamente.";
    emit("sendOutput", exibirresposta.value);
  }
}
</script>

<template>
  <div class="w-auto flex flex-col items-center">
    <textarea
      id="inputText"
      class="textarea textarea-primary"
      placeholder="Input"
      v-model="inputText"
      rows="13"
      cols="80"
    ></textarea>
    <button
      class="btn btn-primary mt-4 py-2 px-16 self-center bg-indigo-600 text-white rounded-md hover:bg-indigo-500 transition"
      @click="prompt"
      :disabled="inputText.trim() === ''"
    >
      Enviar
    </button>
  </div>
</template>
