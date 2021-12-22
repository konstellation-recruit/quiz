import { UPDATE_QUESTION_ID, UPDATE_USER_ID, UPDATE_USER_NAME } from '../constant/action-types';

export const updateUserId = (userId) => ({
    type: UPDATE_USER_ID,
    userId: userId,
});

export const updateUserName = (userName) => ({
    type: UPDATE_USER_NAME,
    userName: userName,
});

export const updateQuestionId = (questionId) => ({
    type: UPDATE_QUESTION_ID,
    questionId: questionId,
});
