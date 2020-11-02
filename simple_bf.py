import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

params = BrainFlowInputParams()
params.other_info = str(BoardIds.CYTON_DAISY_BOARD.value)
board = BoardShim(BoardIds.CYTON_DAISY_BOARD.value, params)
board.prepare_session()