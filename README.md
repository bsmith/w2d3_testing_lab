# Coffee Shop Lab

## Notes from Review:

* The model solutions split the 'buy drink' task into parts that are the
responsibility of the `Customer` and the `CoffeeShop`.
    * This answers the question of where to put `buy_drink`!
    * We wrote the much simpler `reduce_money`.
    * This makes implementing the extensions neater!
* The tests also have a slightly different structure:  we just setup all
of the `CoffeeShop` in `setUp`, but the model solution moves the shop to
the desired state in each test.  Perhaps that works better so it can test
the more basic functions better.
* _Next time_:  more design work, and not just class diagram, but more
focus on interactions
* The model soltuion also takes advantage of `Drink` being 'hashable' and
uses it as the key for the stock dictionary.
    * The reason I don't like this is that it confuses the dictionary for
    two purposes:  holding the `Drink` objects (in the set of keys), and
    holding the stock levels (in the values).
* The model solution also adds some more abstraction for testing things
like adding stock to the shop:  we reach inside and just directly look at
the attribute.
* More summary:  factor, factor, factor!
* From my addition, I wrote `try_removing_stock` which does both a test
and a side-effect.  But I guess confusion comes from slightly woolly
error and exception handling over all so far.

-----

## Todo list:

* ✓ Refactor code!
* ✓ Review MVP brief and check all items completed
* ✓ Refactor code!
* Review Extensions, check all items completed and refactor code
* Refactor code!
* Review Advanced Extensions, complete stock management and refactor code
* Refactor code!

### Extension list:

* Review pub
* Add pubs to model — drawing diagram!
* Implement pubs
* Refactor code!
* Either: Write `app.py` to demonstrate classes working together
* Or: Write an integration test separate from the unit tests

