import { UPDATE_QUESTION_ID, UPDATE_USER_ID } from '../constant/action-types';

const initialState = {
    questionId: 1,
};

const rootReducer = (state = initialState, action) => {
    switch (action.type) {
        case UPDATE_USER_ID:
            return { ...state, userId: action.userId };
        case UPDATE_QUESTION_ID:
            return { ...state, questionId: action.questionId };
        default:
            return state;
    }
};

export default rootReducer;
