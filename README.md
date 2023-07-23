# Etawatch

Like a stopwatch, but it also gives you an ETA.

Example usage:

```python
number_of_laps = 10

# construction immediately starts timer
eta = etawatch(number_of_laps)

for i in range(number_of_laps):
    time.sleep(random.randint(1, 5))
    eta, iteration_time = eta()
    print(f'Time: {iteration_time:.2f} sec | Done in {eta:.2f} min')
```

Another example:

```python
number_of_laps = 10

for i, eta, last_iter_time in enumerate(etawatch(number_of_laps)):
    time.sleep(random.randint(1, 5))
    print(f'Time: {iteration_time:.2f} sec | Done in {eta:.2f} min')
```
