# Lesson 3: Related Rates

## What Are Related Rates and Why Do They Matter?

In the physical world, quantities rarely change in isolation. When a balloon inflates, its volume and its radius change simultaneously. When a ladder slides down a wall, the distance of its base from the wall and the height of its top on the wall change together. When water drains from a conical tank, both the water depth and the surface area of the water change at the same time.

These situations share a common mathematical structure: two or more quantities are linked by a geometric or physical relationship, and all of them change as time passes. The rate at which each quantity changes with respect to time is called a **rate of change** and is written using Leibniz notation as $\frac{d}{dt}$—for example, $\frac{dr}{dt}$ is the rate at which the radius $r$ changes with time, and $\frac{dV}{dt}$ is the rate at which the volume $V$ changes with time.

**Related rates** is the branch of calculus that lets us find one unknown rate of change when we know another rate of change and the equation linking the two quantities. The technique uses implicit differentiation with respect to time $t$ instead of with respect to $x$.

## The Core Idea: Differentiate with Respect to Time

The central mechanism of related rates is to take an equation that relates two or more variables—for example, the Pythagorean theorem $x^2 + y^2 = L^2$ for a ladder of fixed length $L$—and differentiate every term with respect to time $t$. This is an application of implicit differentiation where the variable of differentiation is $t$ rather than $x$.

When we differentiate $x^2$ with respect to $t$, the chain rule gives $2x \cdot \frac{dx}{dt}$. The symbol $\frac{dx}{dt}$ represents the rate at which $x$ changes with time. If $\frac{dx}{dt}$ is positive, $x$ is increasing. If $\frac{dx}{dt}$ is negative, $x$ is decreasing. The same reasoning applies to every variable that changes with time.

A key point: the equation we differentiate is always true at every instant. It is not enough to know the rates of change; we must also know the values of the variables at the specific instant we are interested in. This is a common source of error: students sometimes plug in the rates but forget to compute the instantaneous values of the variables from the original equation.

## The General Strategy for Related Rates Problems

Every related rates problem follows a six-step pattern. Writing these steps explicitly helps avoid mistakes:

1. **Draw a diagram** and label every quantity that changes with time. Use letters for variables and numbers for constants.
2. **Identify what is given and what is unknown.** Write down the known rate (with its sign and units) and the unknown rate you need to find.
3. **Write an equation** that relates the variables. This is usually a geometric formula—the Pythagorean theorem, a volume formula, a similar-triangle proportion.
4. **Differentiate the equation with respect to time $t$.** Every variable that changes gets a chain-rule factor: $\frac{d}{dt}(x^2) = 2x\frac{dx}{dt}$.
5. **Find the instantaneous values of all variables** at the moment of interest. You may need to use the original (undifferentiated) equation for this.
6. **Substitute all known values and solve** for the unknown rate.

A common misconception: many students think they can plug numbers into the equation before differentiating. This is incorrect. You must differentiate the symbolic equation first, then substitute the numbers at the specific instant.

## Worked Examples

### Example 1: The Sliding Ladder

**Problem:** A ladder that is 5 meters long leans against a vertical wall. The bottom of the ladder slides away from the wall at a constant rate of 2 meters per second. How fast is the top of the ladder sliding down the wall at the instant when the bottom is 3 meters from the wall?

**Approach:** To solve this, we need to draw a right triangle with the ladder as the hypotenuse of fixed length 5 m. Let $x$ be the distance from the wall to the bottom of the ladder, and let $y$ be the height of the top of the ladder on the wall. The quantities $x$ and $y$ both change with time. We know $\frac{dx}{dt} = 2$ m/s and we want $\frac{dy}{dt}$ when $x = 3$.

**Step-by-step working:**

The Pythagorean theorem gives the relationship:

$$x^2 + y^2 = 5^2 = 25$$

This equation is true at every instant. Differentiate both sides with respect to $t$:

$$\frac{d}{dt}(x^2) + \frac{d}{dt}(y^2) = \frac{d}{dt}(25)$$

The chain rule gives $2x\frac{dx}{dt}$ for the first term and $2y\frac{dy}{dt}$ for the second. The derivative of the constant $25$ is $0$:

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$

Before we can substitute values, we need $y$ at the instant when $x = 3$. We use the original equation:

$$3^2 + y^2 = 25 \implies 9 + y^2 = 25 \implies y^2 = 16 \implies y = 4$$

The height is $4$ meters (the positive root, since $y$ is a length above the ground).

Now substitute $x = 3$, $y = 4$, and $\frac{dx}{dt} = 2$ into the differentiated equation:

$$2(3)(2) + 2(4)\frac{dy}{dt} = 0$$

$$12 + 8\frac{dy}{dt} = 0$$

$$8\frac{dy}{dt} = -12$$

$$\frac{dy}{dt} = -\frac{12}{8} = -1.5$$

**Why this makes sense:** The top of the ladder slides down at $1.5$ meters per second. The negative sign indicates that $y$ is decreasing, which is what we expect—the height is dropping. Also, $1.5$ is less than $2$, which makes sense because the ladder is longer in the horizontal direction at this instant, so vertical motion is slower than horizontal motion.

---

### Example 2: Inflating a Spherical Balloon

**Problem:** Air is being pumped into a spherical balloon at a rate of $100$ cubic centimeters per second. How fast is the radius of the balloon increasing at the instant when the radius is $5$ centimeters?

**Approach:** To solve this, we relate the volume $V$ and radius $r$ of a sphere using the formula $V = \frac{4}{3}\pi r^3$. We know $\frac{dV}{dt} = 100$ cm³/s and we want $\frac{dr}{dt}$ when $r = 5$.

**Step-by-step working:**

Start with the volume formula:

$$V = \frac{4}{3}\pi r^3$$

Differentiate with respect to $t$. The constant $\frac{4}{3}\pi$ stays in front. The chain rule on $r^3$ gives $3r^2\frac{dr}{dt}$:

$$\frac{dV}{dt} = \frac{4}{3}\pi \cdot 3r^2 \cdot \frac{dr}{dt} = 4\pi r^2 \frac{dr}{dt}$$

Now substitute $\frac{dV}{dt} = 100$ and $r = 5$:

$$100 = 4\pi (5)^2 \frac{dr}{dt}$$

$$100 = 4\pi (25) \frac{dr}{dt}$$

$$100 = 100\pi \frac{dr}{dt}$$

$$\frac{dr}{dt} = \frac{100}{100\pi} = \frac{1}{\pi}$$

**Why this makes sense:** The radius grows at approximately $0.318$ cm/s. This is reasonably slow—the balloon has a moderate surface area at $r = 5$, so adding $100$ cm³ of air per second spreads out over that surface without causing a dramatic change in radius.

---

### Example 3: Water Filling a Conical Tank

**Problem:** A water tank has the shape of an inverted cone with a height of $10$ meters and a base radius of $4$ meters. Water is poured into the tank at a constant rate of $2$ cubic meters per minute. How fast is the water level rising at the instant when the water is $5$ meters deep?

**Approach:** To solve this, we need to relate the volume of water $V$ to the water depth $h$. The complication is that the water forms a smaller cone that is similar to the overall tank. We use similar triangles to express the water-surface radius $r$ in terms of $h$.

**Step-by-step working:**

From similar triangles (the cross-section of the water cone and the full tank cone):

$$\frac{r}{h} = \frac{4}{10} \implies r = \frac{2}{5}h$$

The volume of a cone is $V = \frac{1}{3}\pi r^2 h$. Substitute $r = \frac{2}{5}h$:

$$V = \frac{1}{3}\pi \left(\frac{2}{5}h\right)^2 h = \frac{1}{3}\pi \cdot \frac{4}{25}h^2 \cdot h = \frac{4\pi}{75}h^3$$

Now differentiate with respect to $t$:

$$\frac{dV}{dt} = \frac{4\pi}{75} \cdot 3h^2 \cdot \frac{dh}{dt} = \frac{4\pi}{25}h^2 \frac{dh}{dt}$$

Substitute $\frac{dV}{dt} = 2$ and $h = 5$:

$$2 = \frac{4\pi}{25} \cdot 25 \cdot \frac{dh}{dt}$$

$$2 = 4\pi \frac{dh}{dt}$$

$$\frac{dh}{dt} = \frac{2}{4\pi} = \frac{1}{2\pi}$$

**Why this makes sense:** The water level rises at about $0.159$ meters per minute. The cone widens as depth increases, so at $h = 5$ (half the tank height), the cross-sectional area is substantial, meaning each cubic meter of water added doesn't raise the level by very much.

---

## Practice Problems

### Problem 1
A ladder of length $10$ feet leans against a vertical wall. The top of the ladder is sliding down the wall at $3$ feet per second. How fast is the bottom of the ladder moving away from the wall at the instant when the top of the ladder is $6$ feet above the ground?

### Problem 2
A circular oil slick is spreading on the surface of the ocean. The radius of the slick is increasing at a rate of $2$ meters per minute. At what rate is the area of the slick increasing at the instant when the radius is $10$ meters?

### Problem 3
A spherical balloon is deflating so that its volume decreases at a rate of $50$ cubic centimeters per second. How fast is the radius of the balloon decreasing at the instant when the radius is $10$ centimeters?

### Problem 4
A streetlight is mounted at the top of a pole that is $15$ feet tall. A man who is $6$ feet tall walks away from the pole at a speed of $4$ feet per second along a straight path. How fast is the tip of his shadow moving along the ground at the instant when he is $20$ feet from the base of the pole?

### Problem 5
A cube of ice is melting so that each edge is decreasing at a constant rate of $0.5$ centimeters per minute.
(a) Find the rate at which the volume of the cube is decreasing at the instant when the edge length is $4$ centimeters. [3 marks]
(b) Find the rate at which the surface area of the cube is decreasing at that same instant. [3 marks]
(c) Determine the edge length at the instant when the rate of decrease of the volume is numerically equal to three times the rate of decrease of the surface area. [2 marks]

---

## Answers

### Answer 1

Let $x$ be the distance from the wall to the bottom of the ladder and $y$ be the height of the top. The Pythagorean theorem gives $x^2 + y^2 = 10^2 = 100$. We know $\frac{dy}{dt} = -3$ ft/s (negative because $y$ is decreasing) and we want $\frac{dx}{dt}$ when $y = 6$. First we find $x$ at that instant: $x^2 + 36 = 100$, so $x^2 = 64$ and $x = 8$ ft. Differentiating the Pythagorean equation: $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$. Substituting: $2(8)\frac{dx}{dt} + 2(6)(-3) = 0$, which gives $16\frac{dx}{dt} - 36 = 0$. Solving: $\frac{dx}{dt} = \frac{36}{16} = \frac{9}{4} = 2.25$ ft/s. The bottom of the ladder moves away from the wall at $2.25$ feet per second. A common mistake is to forget the negative sign on $\frac{dy}{dt}$; if you use $+3$ instead of $-3$, you will get a negative value for $\frac{dx}{dt}$, which would incorrectly suggest the bottom moves toward the wall.

### Answer 2

The area of a circle is $A = \pi r^2$. We know $\frac{dr}{dt} = 2$ m/min and we want $\frac{dA}{dt}$ when $r = 10$. Differentiating: $\frac{dA}{dt} = 2\pi r \frac{dr}{dt}$. Substituting: $\frac{dA}{dt} = 2\pi(10)(2) = 40\pi$. The area increases at $40\pi$ square meters per minute, which is approximately $125.7$ m²/min. A common error is to forget the factor of $2$ from the derivative of $r^2$ and write $\pi r \frac{dr}{dt}$ instead of $2\pi r \frac{dr}{dt}$.

### Answer 3

The volume is $V = \frac{4}{3}\pi r^3$. We know $\frac{dV}{dt} = -50$ cm³/s (negative because the balloon is deflating). Differentiating: $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$. Substituting: $-50 = 4\pi(10)^2 \frac{dr}{dt} = 400\pi \frac{dr}{dt}$. Solving: $\frac{dr}{dt} = -\frac{50}{400\pi} = -\frac{1}{8\pi}$ cm/s, which is approximately $-0.0398$ cm/s. The negative sign confirms the radius is decreasing. Be careful to carry the negative sign through the calculation; losing it would give an increasing radius, which contradicts the physical situation.

### Answer 4

Let $x$ be the distance of the man from the base of the pole and let $s$ be the length of his shadow. By similar triangles, $\frac{s}{6} = \frac{x + s}{15}$. Cross-multiplying: $15s = 6x + 6s$, so $9s = 6x$ and $s = \frac{2}{3}x$. The tip of the shadow is at distance $x + s = x + \frac{2}{3}x = \frac{5}{3}x$ from the pole. Differentiating with respect to $t$: the speed of the shadow tip is $\frac{5}{3}\frac{dx}{dt}$. We know $\frac{dx}{dt} = 4$ ft/s, so the shadow tip moves at $\frac{5}{3} \cdot 4 = \frac{20}{3}$ ft/s, approximately $6.67$ ft/s. The man's distance from the pole at that instant ($20$ feet) does not affect this answer because the relationship between shadow tip position and man's position is linear.

### Answer 5

(a) Let $s$ be the edge length. Then $V = s^3$. Differentiating: $\frac{dV}{dt} = 3s^2 \frac{ds}{dt}$. We are given $\frac{ds}{dt} = -0.5$ cm/min (negative because the edge is decreasing). At $s = 4$: $\frac{dV}{dt} = 3(16)(-0.5) = -24$. The volume is decreasing at $24$ cubic centimeters per minute.

(b) The surface area is $A = 6s^2$. Differentiating: $\frac{dA}{dt} = 12s \frac{ds}{dt}$. At $s = 4$: $\frac{dA}{dt} = 12(4)(-0.5) = -24$. The surface area is decreasing at $24$ square centimeters per minute.

(c) We want the edge length $s$ such that the magnitude of $\frac{dV}{dt}$ equals three times the magnitude of $\frac{dA}{dt}$. Since both rates are negative (both are decreasing), the condition is $|\frac{dV}{dt}| = 3|\frac{dA}{dt}|$. Using the differentiated formulas: $3s^2 |\frac{ds}{dt}| = 3 \cdot 12s |\frac{ds}{dt}|$. Cancel $|\frac{ds}{dt}|$ (it is nonzero) and divide both sides by $3s$ (for $s \neq 0$): $s = 12$. At the instant when the edge length is $12$ centimeters, the rate of decrease of volume is numerically three times the rate of decrease of surface area. A common pitfall is to forget the absolute values and mishandle the negative signs.

---

## Key Takeaways

1. Related rates problems connect an unknown rate of change to a known rate through an equation that links the quantities.
2. Always differentiate the symbolic equation first, then substitute the numerical values at the instant of interest. Never plug numbers in before differentiating.
3. The sign of each rate matters: use a positive sign for quantities that are increasing and a negative sign for quantities that are decreasing.
4. You must use the original (undifferentiated) equation to find missing variable values at the specific instant.
5. Drawing a diagram and labeling variables is not optional—it is the most reliable way to set up the correct equation.

