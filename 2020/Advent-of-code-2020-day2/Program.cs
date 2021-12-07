using System;
using System.Linq;

namespace Advent_of_code_2020_day2
{
    class Program
    {
        static void Main(string[] args)
        {
            firstPuzzle();
            secondPuzzle();
        }

        static void firstPuzzle()
        {
            int counter = 0;
            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\2020\Advent-of-code-2020-day2\input.txt"))
            {

                if (line[1] != '-')
                {
                    int lowerBound = (int)Char.GetNumericValue(line[0]) * 10 + (int)Char.GetNumericValue(line[1]);
                    int upperBound = (int)Char.GetNumericValue(line[3]) * 10 + (int)Char.GetNumericValue(line[4]);

                    int freq = line.Count(c => (c == line[6])) - 1;   //so it doesn't count the key letter
                    if (freq >= lowerBound && freq <= upperBound)
                    {
                        counter++;
                    }
                }
                else
                {
                    if (line[3] == ' ')
                    {
                        int lowerBound = (int)Char.GetNumericValue(line[0]);
                        int upperBound = (int)Char.GetNumericValue(line[2]);

                        int freq = line.Count(c => (c == line[4])) - 1;
                        if (freq >= lowerBound && freq <= upperBound)
                        {
                            counter++;
                        }
                    }
                    else
                    {
                        int lowerBound = (int)Char.GetNumericValue(line[0]);
                        int upperBound = (int)Char.GetNumericValue(line[2]) * 10 + (int)Char.GetNumericValue(line[3]);

                        int freq = line.Count(c => (c == line[5])) - 1;
                        if (freq >= lowerBound && freq <= upperBound)
                        {
                            counter++;
                        }
                    }
                }
            }
            Console.WriteLine(counter);
        }

        static void secondPuzzle()
        {
            int counter = 0;
            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\2020\Advent-of-code-2020-day2\input.txt"))
            {

                if (line[1] != '-')
                {
                    int lowerBound = (int)Char.GetNumericValue(line[0]) * 10 + (int)Char.GetNumericValue(line[1]);
                    int upperBound = (int)Char.GetNumericValue(line[3]) * 10 + (int)Char.GetNumericValue(line[4]);

                    if(line[lowerBound + 9] == line[6] || line[upperBound + 9] == line[6])
                    {
                         counter++;
                    } 
                }
                else
                {
                    if (line[3] == ' ')
                    {
                        int lowerBound = (int)Char.GetNumericValue(line[0]);
                        int upperBound = (int)Char.GetNumericValue(line[2]);

                        if (line[lowerBound + 7] == line[4] || line[upperBound + 7] == line[4])
                        {
                            counter++;
                        }
                    }
                    else
                    {
                        int lowerBound = (int)Char.GetNumericValue(line[0]);
                        int upperBound = (int)Char.GetNumericValue(line[2]) * 10 + (int)Char.GetNumericValue(line[3]);

                        if (line[lowerBound + 8] == line[5] || line[upperBound + 8] == line[5])
                        {
                            counter++;
                        }
                    }
                }
            }
            Console.WriteLine(counter);
        }
    }
}

