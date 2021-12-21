import { UPDATE_QUESTION_ID, UPDATE_USER_ID } from '../constant/action-types';

export const updateUserId = (userId) => ({
    type: UPDATE_USER_ID,
    userId: userId,
});

export const updateQuestionId = (questionId) => ({
    type: UPDATE_QUESTION_ID,
    questionId: questionId,
});
