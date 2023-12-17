import unittest
import todo

class MyTestCase(unittest.TestCase):
#
    def test_add_task(self):
        task = "Learn Python"
        task = "Finish project 4 on time"
        task = "Study amply for the final examination"
        todo.add_task(task)

    def test_view_tasks_empty_list(self):
        view_tasks_output = todo.view_tasks()

    def test_view_tasks(self):
        todo.add_task("Learn Python")
        todo.add_task("Join the virtual training")
        todo.view_tasks()

    def test_mark_completed_valid_task(self):
        todo.add_task("Learn Python")
        todo.mark_completed(1)
        self.assertTrue(todo.tasks[0]["completed"])

    def test_mark_completed_invalid_task(self):
        result = todo.mark_completed("1")
        self.assertEqual(result, None)

    def test_delete_task_valid_task(self):
        todo.add_task("Learn Python")
        todo.add_task("Build a To-Do List")
        result = todo.delete_task(1)


if __name__ == "__main__":
    unittest.main()
