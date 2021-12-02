using System;
using System.Collections.Generic;

namespace Advent_of_code_day2
{
    class Program
    {
        static void Main(string[] args)
        {
            secondPuzzle();

        }
        static void firstPuzzle()
        {
                int forward = 0;
                int depth = 0;

                foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\Advent-of-code-day2\input.txt"))
                {
                    if (line.Contains("forward"))
                    {
                        forward += (int)Char.GetNumericValue(line[line.Length - 1]);
                    }
                    else if (line.Contains("up"))
                    {
                        depth -= (int)Char.GetNumericValue(line[line.Length - 1]);
                    }
                    else
                    {
                        depth += (int)Char.GetNumericValue(line[line.Length - 1]);
                    }
                }

                Console.WriteLine($"Units going forward: {forward}");
                Console.WriteLine($"Depth: {depth}");
                Console.WriteLine($"Forward times depth: {forward * depth}");
        }
        

        static void secondPuzzle()
        {
            int forward = 0;
            int depth = 0;
            int aim = 0;

            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\Advent-of-code-day2\input.txt"))
            {
                if (line.Contains("forward"))
                {
                    forward += (int)Char.GetNumericValue(line[line.Length - 1]);
                    depth += aim * (int)Char.GetNumericValue(line[line.Length - 1]);
                }
                else if (line.Contains("up"))
                {
                    aim -= (int)Char.GetNumericValue(line[line.Length - 1]);
                }
                else
                {
                    aim += (int)Char.GetNumericValue(line[line.Length - 1]);
                }
            }

            Console.WriteLine($"Units going forward: {forward}");
            Console.WriteLine($"Depth: {depth}");
            Console.WriteLine($"Forward times depth: {forward * depth}");
        }

    }
}
