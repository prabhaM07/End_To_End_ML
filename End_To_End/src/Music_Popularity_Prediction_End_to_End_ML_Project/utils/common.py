import os
import yaml
import json
import joblib
from box import ConfigBox
from Music_Popularity_Prediction_End_to_End_ML_Project import logger
from typing import Any


def read_yaml(path_to_yaml: str) -> ConfigBox:
    """Reads YAML file and returns as ConfigBox.

    Args:
        path_to_yaml (str): Path to YAML file.

    Raises:
        ValueError: If YAML file is empty or cannot be loaded.

    Returns:
        ConfigBox: ConfigBox object containing YAML content.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file '{path_to_yaml}': {e}")
    except Exception as e:
        raise ValueError(f"Failed to load YAML file '{path_to_yaml}': {e}")


def create_directories(path_to_directories: list[str], verbose: bool = True):
    """Create directories given a list of paths.

    Args:
        path_to_directories (list[str]): List of paths to create directories.
        verbose (bool, optional): Whether to log verbose messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: str, data: dict):
    """Save data to a JSON file.

    Args:
        path (str): Path to JSON file.
        data (dict): Data to be saved.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"JSON file saved at: {path}")


def load_bin(path: str) -> Any:
    """Load binary data from a file.

    Args:
        path (str): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def get_size(path: str) -> str:
    """Get file size in KB.

    Args:
        path (str): Path of the file.

    Returns:
        str: Size of the file in KB (formatted string).
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
