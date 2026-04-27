"""
Unit tests for app.main module functions.
Tests the fetch_all_tasks utility function with various scenarios.
"""

import asyncio
import pytest
from typing import List
from unittest.mock import patch, MagicMock

from app.main import fetch_all_tasks, MOCK_TASKS
from app.models import DeveloperTask, TaskStatus


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_list_of_developer_tasks() -> None:
    """Test that fetch_all_tasks returns a list of DeveloperTask objects."""
    result: List[DeveloperTask] = await fetch_all_tasks()
    
    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Result should contain tasks"
    assert all(isinstance(task, DeveloperTask) for task in result), \
        "All items should be DeveloperTask instances"


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_all_mock_tasks() -> None:
    """Test that fetch_all_tasks returns all tasks from MOCK_TASKS."""
    result: List[DeveloperTask] = await fetch_all_tasks()
    expected_count: int = len(MOCK_TASKS)
    
    assert len(result) == expected_count, \
        f"Expected {expected_count} tasks, got {len(result)}"


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_correct_task_data() -> None:
    """Test that returned tasks contain correct data matching MOCK_TASKS."""
    result: List[DeveloperTask] = await fetch_all_tasks()
    mock_task_ids: set = {task.task_id for task in result}
    expected_ids: set = set(MOCK_TASKS.keys())
    
    assert mock_task_ids == expected_ids, \
        f"Task IDs should match MOCK_TASKS keys. Got {mock_task_ids}, expected {expected_ids}"
    
    # Verify task properties match
    for returned_task in result:
        original_task: DeveloperTask = MOCK_TASKS[returned_task.task_id]
        assert returned_task.title == original_task.title, \
            f"Task {returned_task.task_id} title mismatch"
        assert returned_task.status == original_task.status, \
            f"Task {returned_task.task_id} status mismatch"
        assert returned_task.hours_spent == original_task.hours_spent, \
            f"Task {returned_task.task_id} hours_spent mismatch"


@pytest.mark.asyncio
async def test_fetch_all_tasks_with_empty_mock_tasks() -> None:
    """Test that fetch_all_tasks returns empty list when MOCK_TASKS is empty."""
    with patch("app.main.MOCK_TASKS", {}):
        result: List[DeveloperTask] = await fetch_all_tasks()
        
        assert isinstance(result, list), "Result should be a list"
        assert len(result) == 0, "Result should be empty when MOCK_TASKS is empty"


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_independent_copy() -> None:
    """Test that modifying returned list doesn't affect MOCK_TASKS."""
    result: List[DeveloperTask] = await fetch_all_tasks()
    original_count: int = len(MOCK_TASKS)
    
    # Modify the returned list
    result.clear()
    
    # MOCK_TASKS should remain unchanged
    assert len(MOCK_TASKS) == original_count, \
        "Modifying returned list should not affect MOCK_TASKS"
    
    # Verify we can still fetch all original tasks
    result_after: List[DeveloperTask] = await fetch_all_tasks()
    assert len(result_after) == original_count, \
        "Subsequent fetch should return all original tasks"


@pytest.mark.asyncio
async def test_fetch_all_tasks_is_async() -> None:
    """Test that fetch_all_tasks is a proper async function."""
    # Create the coroutine
    coro = fetch_all_tasks()
    
    # Verify it's a coroutine
    assert asyncio.iscoroutine(coro), "fetch_all_tasks should return a coroutine"
    
    # Clean up the coroutine
    await coro
