import re

#Declaring variables with default values
count_of_sentences = 0
count_of_words = 0
count_of_letters = 0

#Reading input text file
with open('Resources/paragraph_2.txt', 'r',encoding='utf-8') as input_file:
    for row in input_file:
        row = row.replace('“','')
        row = row.replace('”','')
        sentences = re.split('[.\n?]', row)
        #Counting the number of sentences, words and letters from input file
        for sentence in sentences:
            words = re.split('[-–\',()<>1234567890\" ]', sentence)
            count_word = 0
            for word in words:
                if len(word) > 0:
                    count_word += 1
                    count_of_letters += len(word)

            if count_word > 0:
                count_of_words += count_word
                count_of_sentences += 1

#Declaring the list variable to print the Paragraph Analysis results
results = []
#Appending the required output for the results list variable
results.append("Paragraph Analysis\n-----------------")
results.append(f"Approximate Word Count: {count_of_words}")
results.append(f"Approximate Sentence Count: {count_of_sentences}")
results.append(f"Average Letter Count: {round(count_of_letters/count_of_words,1)}")
results.append(f"Average Sentence Length: {round(count_of_words/count_of_sentences,1)}")

filename = 'Analysis/paragraph_analysis_results.txt'
#Exporting the output into text file
with open(filename, 'w') as output_file:
    for result in results:
        print(result)
        output_file.write(result + '\n')