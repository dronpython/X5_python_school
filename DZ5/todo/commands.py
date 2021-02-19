
from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    @property
    def label(self) -> str:
        raise NotImplementedError()

    def perform(self, store):
        raise NotImplementedError()


class ListCommand(BaseCommand):
    label = 'list'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(store.items):
            print('{0}: {1}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    label = 'new'

    def perform(self, store):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{0}: {1}'.format(index, name))

        selection = None
        selected_key = None

        while True:
            try:
                selected_key = self._select_item(classes)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        selected_class = classes[selected_key]
        print('Selected: {0}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        store.items.append(new_object)
        print('Added {0}'.format(str(new_object)))
        print()
        return new_object

    @classmethod
    def _load_item_classes(cls) -> dict:
        # Dynamic load:
        classes = find_classes(BaseItem)
        return dict(classes)

    def _select_item(self, classes):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return list(classes.keys())[selection]


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')


class DoneCommand(BaseCommand):
    label = 'done'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        print('Choose task to done:')
        for index, obj in enumerate(store.items):
            print('{0}: {1}'.format(index, str(obj)))

        while True:
            try:
                selected_task = self._select_item(store)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break
        selected_task.done = True
        print(f'Task "{selected_task.heading}" done!')

    def _select_item(self, store):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return store.items[selection]


class UndoneCommand(BaseCommand):
    label = 'undone'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        print('Choose task to undone:')
        for index, obj in enumerate(store.items):
            print('{0}: {1}'.format(index, str(obj)))

        while True:
            try:
                selected_task = self._select_item(store)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break
        selected_task.done = False
        print(f'Task "{selected_task.heading}" undone:(')

    def _select_item(self, store):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return store.items[selection]
