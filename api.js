import { GoogleGenerativeAI } from "@google/generative-ai";
import express from "express";
import cors from "cors";
import "dotenv/config";

const promptData = await fetch("../src/assets/prompt.json").then((res) =>
  res.json()
);
const port = process.env.PORT || 3000;
const app = express();

const key = process.env.GOOGLE_GEN_AI_KEY;
const genAI = new GoogleGenerativeAI(key);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

app.use(cors());
app.use(express.json());

app.post("/prompt", async (req, res) => {
  try {
    const { inputText } = req.body;

    const prompt = `
            ${promptData.instruction}
            ${Object.entries(promptData.details)
              .map(([key, value]) => `${key}: ${value}`)
              .join("\n")}
            Informação adicional: ${inputText}
            Formato esperado: ${promptData.format}
        `;

    const result = await model.generateContent(prompt);
    const responseText = await result.response.text();

    res.json({ response: responseText, success: true });
  } catch (error) {
    console.error("Erro ao enviar resposta:", error);
    res.status(500).json({
      response: "Erro ao processar a resposta. Tente novamente.",
      success: false,
    });
  }
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
