import {
    UPDATE_QUESTION_ID,
    UPDATE_TRUE_NUMBER,
    UPDATE_FALSE_NUMBER,
    UPDATE_USER_SCORE,
    UPDATE_QUESTION_DATA,
    UPDATE_USER_ID,
    UPDATE_USER_NAME,
    UPDATE_STATUS,
    UPDATE_IMAGE,
} from '../constant/action-types';

const initialState = {
    questionId: 1,
    userScore: [],
};

const rootReducer = (state = initialState, action) => {
    switch (action.type) {
        case UPDATE_USER_ID:
            return { ...state, userId: action.userId };
        case UPDATE_USER_NAME:
            return { ...state, userName: action.userName };
        case UPDATE_QUESTION_ID:
            return { ...state, questionId: action.questionId };
        case UPDATE_QUESTION_DATA:
            return { ...state, questionData: action.questionData };
        case UPDATE_USER_SCORE:
            return { ...state, userScore: action.userScore };
        case UPDATE_TRUE_NUMBER:
            return { ...state, trueNumber: action.trueNumber };
        case UPDATE_FALSE_NUMBER:
            return { ...state, falseNumber: action.falseNumber };
        case UPDATE_STATUS:
            return { ...state, status: action.status };
        case UPDATE_IMAGE:
            return { ...state, image: action.image };
        default:
            return state;
    }
};

export default rootReducer;
