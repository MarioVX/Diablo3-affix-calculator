# Diablo 3 Affix Distribution and Enchantability Calculator

Python tool to compute the probability distribution over affix combinations for a given item, and chance that it generates with an affix combination that can be enchanted into a desired combination.

## Usage
- Use with Python in interactive mode.
- Call help() on distribution() or check_enchantable(), depending on which you want to use.
- If the item of interest is not yet registered in "items", add an entry for it.
- Call distribution() or check_enchantable() with affix combinations of interest.
- If you mistrust the datamined affix weights, use assume_uniform() before calling either to override the weights to be uniform instead.
- Outputs probabilities as exact fractions. If such a number is unwieldy, convert with float().
