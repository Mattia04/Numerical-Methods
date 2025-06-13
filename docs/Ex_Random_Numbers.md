# Exercises on random numbers

## 1. Sierpinski Triangle

There is a surprising way to generate an image of the [Sieripinski triangle](https://en.wikipedia.org/wiki/Sierpiński_triangle) using random numbers.

!!! abstract "Generation"
    Construct an equilateral triangle with labeled vertices, for example `1`, `2` and `3`.
    
    We start selecting a random point on the plane.

    Now we generate a random number between 1 and 3 (extremes included), and we draw a point in the middle point of the previous point and the vertex corrisponding to the random number generated.
    The new point generated would be used by the next iteration.

    We then repeat the process (`random number -> draw midpoint -> ...`) for a predefined large number of times like $N \sim 10000$ or more.

!!! note 
    Since we are going to increase the number of sides of our figure, making the code modular for the number of sides is a good idea.

??? success "Result"
    This is the result you will get

??? tip "Getting a better result"
    Since by starting on a random point would give us the first few points on noticiable "wrong" positions we can get a nicer result by skipping the first few points.

    One can also calculate the error $\Delta$ of the points from their actual position on the triangle after deleting the firsts $n$ points using the formula:
    $$ \Delta \approx \frac{\ell}{2^n} $$
    Where $\ell$ is the length of the triangle side. Note: this formula works only if the point is inside or near the triangle.

    We can notice that after the first $n = 10$ iterations we have an error around 1000 times smaller, so we can decide to not draw the first 10 points and get a better result without compromising computational time (we loose only 10 points out of 10000 which is only 0.1% of the total points).

??? tip "Making an animation"
    We could also make a simple animation by updating the plot frame after each point drawn.

    This is left as an excercise to the interested reader.

    ??? success "Example"
        Insert animation here

## 2. Sierpinski Square

What happens when we increase the number of sides from 3 to 4 adding a fourth label to our random number generator, and we keep drawing the midpoint?

??? Failure "Filled Square?"
    By running the code you will notice that with this method we will get a filled square, which is not what we want.

    The fix is actually really simple can you think what we should change?
    
    ??? tip "Tip 1 out of 2"
        We want to get a hole in the middle, so we should change the distance from the previous point where we generate the new point.
        We want the new point to be located at 1/3 (from the vertex) of the segment connecting the random vertex from the previous point.

        Implementing this is easy, from taking the middle point, which is the average. We take the weighted average with weights: 2 on the vertex and 1 on the previous point.

        But this also does not gives us the result we attended, this gives us a cross in the middle but we want a hole.

    ??? tip "Tip 2 out of 2"
        To get a hole instead of a cross we would need to add 4 new generation points, each one located in the middle point of the square sides.

??? success "Result"
    this is the correct result

## 3. Koch Snowflake

Let's try making something similar, but different.

Take an exagon, with labeled vertices, and the wighted average for generating the new point (with weights: 2 on the vertex and 1 on the previous point).
With this rules you will get a different structure called the [Koch Snowflake](https://en.wikipedia.org/wiki/Koch_snowflake).

??? success "Result"
    insert photo here.

## 4. Changing the number of dimensions.

What happens when we just generate points on one line? We get the [Cantor Set](https://en.wikipedia.org/wiki/Cantor_set).

!!! Note 
    When we first generated the Sierpinski Square in "Tip 1 out of 2", we generated the two dimensional Cantor Set.

### 4.1. Cantor Set

To generate the cantor set we just need 2 points and the weighted average at 2 to 1 weights like before.

??? success "Result"
    Insert image here.

We went down in dimensions can we go up? Yes, but the number of points we need to generate will increase a lot ($N\sim 10^6$).

### 4.2. Tetrahedron

??? success "Result"
    Insert image here.

### 4.3. Cube

??? success "Result"
    Insert image here.

### 4.4. Dodecahedron

??? success "Result"
    Insert image here.

## 5. A more Efficient Way of doing all of this

Affine Iterated Function System (IFS)

### 5.1. Dodecahedron with more resolution

### 5.2. Generating leafs and trees
