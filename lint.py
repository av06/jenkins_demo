from pylint.lint import Run

results = Run(['app.py','bubblesort.py'], do_exit=False)
print("App Stats: ",results.linter.stats['by_module']['app'])
print("Bubblesort Stats: ",results.linter.stats['by_module']['bubblesort'])
print("Overall Score: ",results.linter.stats['global_note'])
