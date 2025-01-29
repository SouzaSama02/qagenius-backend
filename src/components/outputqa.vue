<script setup>
import { defineProps } from "vue";

defineProps({
  dados: {
    type: Object,
    required: true,
    default: "",
  },
});
</script>

<template>
  <div class="w-auto h-5/6 flex flex-col items-center mb-16">
    <textarea
      v-if="dados"
      class="textarea textarea-primary w-full h-full"
      rows="13"
      cols="80"
      v-model="dados.response"
    >
    </textarea>
    <p v-else class="text-gray-500 italic text-center px-4">
      Nenhuma resposta disponível.
    </p>
  </div>
</template>
