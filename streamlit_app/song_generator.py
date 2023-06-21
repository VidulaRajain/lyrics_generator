
import openai
import os


class LyricsGenerator():


    def preprocess(self):
       self.prompt =  self.input_verse + '\n' + self.input_lyrics + "\n\n### \n\n"


    def generate(self):
        openai.api_key = self.api_key

        response = openai.Completion.create(
        model="davinci:ft-personal:lyrics-generator-1-2023-06-19-18-00-56",
        prompt = self.prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["END"]
        )

        
        self.generations = response['choices'][0]['text']

   
    def run(self, key, input_lyrics, input_verse="[Verse 1]"):

        try:
            self.api_key = key
            self.input_lyrics = input_lyrics
            self.input_verse = input_verse
            
            self.preprocess()
            self.generate()

            return self.generations

        except Exception as exc:
            return 'Request Failed'



if __name__ == '__main__':
    pass