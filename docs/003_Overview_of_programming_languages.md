# Overview of Programming Languages

There are a lot of programming languages out there, every one of them with 
their pros and cons, in this guide we will focus on `python`, but in this 
page we will also talk a little about: `Fortran`, `C`, `C++`, `R`, `MATLAB`, 
`Mathematica (wolfram)`, `Julia`. 

During the first part of the course we will 
forget 
about those languages, we will talk about them later we will need to 
integrate advanced tools in our projects.

We will not discuss other languages.

??? info "Honorable mentions:"

    There are some cool programming languages out there like:  `Assembly`, 
    `Haskell`, `Rust`
    `Java` (not honorable but I have to cite it) and `brainfuck`. 

## Why python?

Let me explain why I choose phyton as the main focus of this guide. I will 
explain with an example.

Let's imagine we want to calculate the trajectory of a free-falling body, in 
particular we want to calculate the time of flight, the maximum height and 
the horizontal distance given: the initial velocity, the initial angle and 
the gravitational acceleration.

We will create a file called `input.txt` where we will write our initial 
parameters.

??? abstract "input.txt"

        velocity: 30
        angle: 45
        gravity: 9.8

We will now want to create a program to read the file and solve our problem, 
below are 7 solutions in different languages.

!!! example "Solutions"

    === "python"
    
        ```py title="example.py"
        import math
        
        # calculate trajectory parameters
        def calculate_projectile(velocity, angle_deg, gravity):
            angle_rad = math.radians(angle_deg)
            
            time_of_flight = (2 * velocity * math.sin(angle_rad)) / gravity
            
            max_height = (velocity**2 * math.sin(angle_rad)**2) / (2 * gravity)
            
            horizontal_distance = (velocity**2 * math.sin(2 * angle_rad)) / gravity
            
            return time_of_flight, max_height, horizontal_distance
        
        # Read inputs from file
        input_file = 'input.txt'
        try:
            with open(input_file, 'r') as file:
                data = file.readlines()
                inputs = {}
                for line in data:
                    key, value = line.split(':')
                    inputs[key.strip()] = float(value.strip())
            
            # Extract values from input dictionary
            velocity = inputs['velocity']
            angle = inputs['angle']
            gravity = inputs['gravity']
            
            # Calculate results
            time_of_flight, max_height, horizontal_distance = calculate_projectile(velocity, angle, gravity)
            
            # Print results
            print(f"Time of Flight: {time_of_flight:.2f} seconds")
            print(f"Maximum Height: {max_height:.2f} meters")
            print(f"Horizontal Distance: {horizontal_distance:.2f} meters")
        
        except FileNotFoundError:
            print(f"Error: Input file '{input_file}' not found.")
        ```
        
        Run:
    
            python example.py
    
    
    === "C++"
    
        ```cpp title="example.cpp"
        #include <iostream>
        #include <fstream>
        #include <cmath>
        #include <string>
        
        using namespace std;
        
        // Function to calculate the projectile motion
        void calculateProjectile(double velocity, double angle_deg, double gravity,
                                 double &time_of_flight, double &max_height, double &horizontal_distance) {
            double angle_rad = angle_deg * M_PI / 180.0;
        
            time_of_flight = (2 * velocity * sin(angle_rad)) / gravity;
        
            max_height = (pow(velocity, 2) * pow(sin(angle_rad), 2)) / (2 * gravity);
        
            horizontal_distance = (pow(velocity, 2) * sin(2 * angle_rad)) / gravity;
        }
        
        int main() {
            // Input file name
            string input_file = "input.txt";
            ifstream infile(input_file);
        
            if (!infile.is_open()) {
                cerr << "Error: Unable to open input file \"" << input_file << "\"." << endl;
                return 1;
            }
        
            // Read inputs
            double velocity, angle, gravity;
            string line;
            while (getline(infile, line)) {
                size_t delimiter = line.find(':');
                string key = line.substr(0, delimiter);
                double value = stod(line.substr(delimiter + 1));
                
                
                if (key == "velocity") velocity = value;
                else if (key == "angle") angle = value;
                else if (key == "gravity") gravity = value;
            }
            infile.close();
        
            double time_of_flight, max_height, horizontal_distance;
        
            // Perform calculations
            calculateProjectile(velocity, angle, gravity, time_of_flight, max_height, horizontal_distance);
        
            // Output results
            cout << "Time of Flight: " << time_of_flight << " seconds" << endl;
            cout << "Maximum Height: " << max_height << " meters" << endl;
            cout << "Horizontal Distance: " << horizontal_distance << " meters" << endl;
        
            return 0;
        }
        ```
    
        Compilation:
    
            g++ -o example example.cpp
    
        Execution:
    
            ./example
    
    === "MATLAB"
    
        ```matlab title="example.m"
        input_file = 'input.txt';
        
        % Read the file
        try
            fileID = fopen(input_file, 'r');
            data = textscan(fileID, '%s %f', 'Delimiter', ':');
            fclose(fileID);
            
            % Parse inputs
            inputs = containers.Map(data{1}, data{2});
            velocity = inputs('velocity');
            angle = inputs('angle');
            gravity = inputs('gravity');
            
            angle_rad = deg2rad(angle);
            
            time_of_flight = (2 * velocity * sin(angle_rad)) / gravity;
            
            max_height = (velocity^2 * (sin(angle_rad)^2)) / (2 * gravity);
            
            horizontal_distance = (velocity^2 * sin(2 * angle_rad)) / gravity;
            
            % Display results
            fprintf('Time of Flight: %.2f seconds\n', time_of_flight);
            fprintf('Maximum Height: %.2f meters\n', max_height);
            fprintf('Horizontal Distance: %.2f meters\n', horizontal_distance);
        
        catch ME
            fprintf('Error reading or processing the input file: %s\n', ME.message);
        end
        ```
    
        Run (in MATLAB or Octave):
            
            example
    
    === "Fortran"
            
        ```fortran title="example.f90"
        program projectile
            implicit none
        
            real(8) :: velocity, angle, gravity
            real(8) :: time_of_flight, max_height, horizontal_distance
            character(len=100) :: line
            integer :: iunit, ios
            character(len=20) :: key
            real(8) :: value
        
            open(unit=iunit, file='input.txt', status='old')
        
            ! Read the input file line by line
            do
                read(iunit,'(A)', i=1) line
                if (line == '') exit
                
                read(line, '(A:F)', iunit=ios, i=1) key, value
                select case (key)
                case ("velocity")
                    velocity = value
                case ("angle")
                    angle = value
                case ("gravity")
                    gravity = value
                end select
            end do
            close(iunit)
        
            ! Perform calculations
            time_of_flight = (2.0 * velocity * sin(angle * 3.141592653589793 / 180.0)) / gravity
            max_height = (velocity**2 * sin(angle * 3.141592653589793 / 180.0)**2) / (2.0 * gravity)
            horizontal_distance = (velocity**2 * sin(2.0 * angle * 3.141592653589793 / 180.0)) / gravity
        
            ! Output results
            print *, 'Time of Flight: ', time_of_flight, ' seconds'
            print *, 'Maximum Height: ', max_height, ' meters'
            print *, 'Horizontal Distance: ', horizontal_distance, ' meters'
        
        end program projectile
        ```
    
        Compilation:
    
            gfortran -o example example.f90
    
        Execution:
    
            ./example
    
    === "Julia"
    
        ```julia title="example.jl"
        # Function to calculate projectile motion
        function calculate_projectile(velocity, angle_deg, gravity)
            angle_rad = deg2rad(angle_deg)
            
            time_of_flight = (2 * velocity * sin(angle_rad)) / gravity
            
            max_height = (velocity^2 * sin(angle_rad)^2) / (2 * gravity)
            
            horizontal_distance = (velocity^2 * sin(2 * angle_rad)) / gravity
            
            return time_of_flight, max_height, horizontal_distance
        end
        
        # Read input from file
        function read_input(file_name)
            inputs = Dict{String, Float64}()
            open(file_name, "r") do f
                for line in eachline(f)
                    parts = split(line, ":")
                    key = strip(parts[1])
                    value = parse(Float64, strip(parts[2]))
                    inputs[key] = value
                end
            end
            return inputs
        end
        
        input_file = "input.txt"
        inputs = read_input(input_file)
        
        # Extract values
        velocity = inputs["velocity"]
        angle = inputs["angle"]
        gravity = inputs["gravity"]
        
        # Perform calculations
        time_of_flight, max_height, horizontal_distance = calculate_projectile(velocity, angle, gravity)
        
        # Output results
        println("Time of Flight: ", time_of_flight, " seconds")
        println("Maximum Height: ", max_height, " meters")
        println("Horizontal Distance: ", horizontal_distance, " meters")
        ```
    
        Run:
        
            julia example.jl
    
    === "Mathematica"
            
        ```mathematica title="example.wls"
        (* Function to calculate projectile motion *)
        calculateProjectile[velocity_, angle_, gravity_] := Module[
          {timeOfFlight, maxHeight, horizontalDistance, angleRad},
          
          angleRad = AngleUnit -> Degree;
          
          timeOfFlight = (2 velocity Sin[angle]) / gravity;
          
          maxHeight = (velocity^2 Sin[angle]^2) / (2 gravity);
          
          horizontalDistance = (velocity^2 Sin[2 angle]) / gravity;
          
          {timeOfFlight, maxHeight, horizontalDistance}
        ]
        
        (* Function to read inputs from file *)
        readInput[file_] := Module[
          {lines, inputs},
          lines = ReadList[file, String];
          inputs = Association[];
          Do[
            (* Parse key-value pairs from each line *)
            inputs[key] = ToExpression[StringDrop[lines[[i]], 1]],
            {i, Length[lines]},
            {key, StringTake[lines[[i]], {1, 7}]}
          ];
          inputs
        ]
        
        (* Main program *)
        
        (* Read input file *)
        inputFile = "input.txt";
        inputs = readInput[inputFile];
        
        (* Extract values *)
        velocity = inputs["velocity"];
        angle = inputs["angle"];
        gravity = inputs["gravity"];
        
        (* Perform calculations *)
        {timeOfFlight, maxHeight, horizontalDistance} = calculateProjectile[velocity, angle, gravity];
        
        (* Output results *)
        Print["Time of Flight: ", timeOfFlight, " seconds"];
        Print["Maximum Height: ", maxHeight, " meters"];
        Print["Horizontal Distance: ", horizontalDistance, " meters"];
        ```
    
        Run:
    
            math -script example.wls
    
    === "R"
    
        ```R title="example.R"
        # Function to calculate projectile motion
        calculate_projectile <- function(velocity, angle_deg, gravity) {
          # Convert angle to radians
          angle_rad <- angle_deg * pi / 180
          
          time_of_flight <- (2 * velocity * sin(angle_rad)) / gravity
          
          max_height <- (velocity^2 * sin(angle_rad)^2) / (2 * gravity)
          
          horizontal_distance <- (velocity^2 * sin(2 * angle_rad)) / gravity
          
          return(list(time_of_flight = time_of_flight, 
                      max_height = max_height, 
                      horizontal_distance = horizontal_distance))
        }
        
        # Function to read input from file
        read_input <- function(file_name) {
          lines <- readLines(file_name)
          
          # Extract key-value pairs
          inputs <- sapply(lines, function(line) {
            parts <- strsplit(line, ":")[[1]]
            key <- trimws(parts[1])
            value <- as.numeric(trimws(parts[2]))
            return(value)
          })
          
          # Return a named list
        return(setNames(as.list(inputs), c("velocity", "angle", "gravity")))
        }
        
        # Main program
        input_file <- "input.txt"
        
        # Read inputs
        inputs <- read_input(input_file)
        
        # Perform calculations
        results <- calculate_projectile(inputs$velocity, inputs$angle, inputs$gravity)
        
        # Print results
        cat("Time of Flight:", results$time_of_flight, "seconds\n")
        cat("Maximum Height:", results$max_height, "meters\n")
        cat("Horizontal Distance:", results$horizontal_distance, "meters\n")
        ```
    
        Run:
        
            Rscript example.R

??? help "If you cannot understand the code"

    If it's the first time seeing source code don't worry, it's like trying 
    to understand some phrases in a language that you don't know, what do 
    you expect?  
    Learning to code is a slow process, you will be able to understand 
    everything step by step following this guide.

As you can see each language has a different syntax, from the seven the 
most intuitive language is python (with julia and R pretty colse). That's 
the main reason why this guide is in python it is **easy to read**.

## Pros and cons of python

### Pros
- **Ease of Learning**: Python's simple syntax makes it beginner-friendly.
- **Versatility**: Wide applicability in web development, data science, machine learning, automation, and more.
- **Large Ecosystem**: Extensive libraries and frameworks (e.g., NumPy, pandas, TensorFlow, Flask, Django).
- **Cross-Platform**: Works seamlessly across multiple operating systems.
- **Community Support**: Large and active community ensures plenty of resources and troubleshooting support.
- **Interpreted Language**: Eliminates the need for compilation, facilitating rapid development and testing.
- **Dynamic Typing**: Allows flexibility in variable usage without strict type declarations.
- **Integration Capability**: Easily integrates with other languages like C, C++, and Java.
- **Readable Code**: Emphasizes code readability, which is critical for collaborative projects.
- **Strong Support for Automation**: Simplifies scripting and task automation.

### Cons
- **Slower Execution**: Interpreted nature and dynamic typing can make it slower compared to compiled languages like C++ or Java.
- **High Memory Usage**: May not be suitable for memory-intensive tasks.
- **Weak in Mobile Development**: Limited adoption for mobile application development.
- **Runtime Errors**: Dynamic typing can lead to runtime errors that might be caught earlier in statically typed languages.
- **GIL (Global Interpreter Lock)**: Limits the performance of multithreaded Python programs, especially in CPU-bound tasks.
- **Version Compatibility Issues**: Migration between Python 2 and Python 3 caused fragmentation; legacy issues may persist.
- **Not Ideal for Low-Level Programming**: Less efficient for tasks requiring direct interaction with hardware.

## Let's talk about the others

`C`: A low-level, efficient, and widely-used programming language for system programming, embedded systems, and performance-critical applications.

`C++`: An extension of C, adding object-oriented programming, templates, and modern programming paradigms, used for high-performance applications.

`Fortran`: A high-performance language for scientific and numerical computing, particularly in physics, engineering, and computational simulations.

`R`: A language designed for statistical analysis and data visualization, widely used in data science and research.

`MATLAB`: A high-level language and environment for numerical computing, data analysis, and visualization, popular in engineering and scientific domains.

`Mathematica`: A symbolic computation and numerical analysis tool with powerful capabilities for algebra, calculus, and advanced scientific visualization.

`Julia`: A modern, high-performance language designed for numerical and scientific computing, offering simplicity and speed.