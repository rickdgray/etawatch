# Etawatch

Like a stopwatch, but it also gives you an ETA.

Example usage:

```python
# construction immediately starts timer
eta_watch = etawatch(5)
for i in range(number_of_laps):
    # do some work
    time.sleep(random.randint(1, 3))
    eta, lap = eta_watch()
    print(f'Lap: {i+1} | Time: {lap:.2f} sec | ETA: {eta:.2f} min')
```

Another example:

```python
for i, (eta, lap) in enumerate(etawatch(5)):
    # do some work
    time.sleep(random.randint(1, 3))
    print(f'Lap: {i+1} | Time: {lap:.2f} sec | ETA: {eta:.2f} min')
```

It can optionally predict ETA by only the last `n` number of runs.

```python
# will only calculate ETAs based on last 3 lap times
eta = etawatch(10, 3)
```
