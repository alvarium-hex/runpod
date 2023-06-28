"""
RunPod | Transformer | Model Fetcher
"""

import argparse
import os
from huggingface_hub import snapshot_download

def download_model(model_name):
    # --------------------------------- Neo 1.3B --------------------------------- #
    if model_name == "gpt-neo-1.3B":
        snapshot_download(repo_id="EleutherAI/gpt-neo-1.3B", repo_type="model")

    # --------------------------------- Neo 2.7B --------------------------------- #
    elif model_name == "gpt-neo-2.7B":
        snapshot_download(repo_id="EleutherAI/gpt-neo-2.7B", repo_type="model")

    # ----------------------------------- NeoX ----------------------------------- #
    elif model_name == "gpt-neox-20b":
        snapshot_download(repo_id="EleutherAI/gpt-neox-20b", repo_type="model")

    # --------------------------------- Pygmalion -------------------------------- #
    elif model_name == "pygmalion-6b":
        snapshot_download(repo_id="PygmalionAI/pygmalion-6b", repo_type="model")

    # ----------------------------------- GPT-J ----------------------------------- #
    elif model_name == "gpt-j-6b":
        snapshot_download(
            repo_id="EleutherAI/gpt-j-6B", revision="float16", repo_type="model"
        )

# ---------------------------------------------------------------------------- #
#                                Parse Arguments                               #
# ---------------------------------------------------------------------------- #
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--model_name",
    type=str,
    default="gpt-neo-1.3B",
    help="URL of the model to download.",
)


if __name__ == "__main__":
    args = parser.parse_args()
    download_model(args.model_name)
