#!/usr/bin/python
import sublime_plugin

def find_where_to_undo_select_lines(view):
    result = None
    # Looking for a few items in history for the one with "select_lines"
    for i in range(0,-42,-1):
        history_item = view.command_history(i)
        if history_item[0] == "select_lines":
            result = history_item[1]["forward"]
            break
        elif history_item[0] != "undo_select_lines":
            break
    return result

class UndoSelectLinesContext(sublime_plugin.EventListener):
    def on_query_context(self, view, key, *args):
        if key != "undo_select_lines":
            return None

        # We don't need to do anything if there is only one caret
        if len(view.sel()) == 1:
            return None

        # If we can't find what to undo, don't do anything
        if find_where_to_undo_select_lines(view) == None:
            return None

        # Hack: I couldn't find a way not to place this "undo" action
        # to the history, so I undo all the things when we come to two regions
        if len(view.sel()) == 2:
            view.run_command("soft_undo")
            return None
        else:
            return True

class UndoSelectLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if self.view.command_history(0)[1] and self.view.command_history(0)[1]["forward"]:
            sel.subtract(sel[-1])
        else:
            sel.subtract(sel[0])
