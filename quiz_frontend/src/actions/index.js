import {
    UPDATE_QUESTION_DATA,
    UPDATE_FALSE_NUMBER,
    UPDATE_TRUE_NUMBER,
    UPDATE_USER_SCORE,
    UPDATE_QUESTION_ID,
    UPDATE_USER_ID,
    UPDATE_USER_NAME,
    UPDATE_STATUS,
    UPDATE_IMAGE,
} from '../constant/action-types';

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

export const updateQuestionData = (questionData) => ({
    type: UPDATE_QUESTION_DATA,
    questionData: questionData,
});

export const updateUserScore = (userScore) => ({
    type: UPDATE_USER_SCORE,
    userScore: userScore,
});

export const updateTrueNumber = (trueNumber) => ({
    type: UPDATE_TRUE_NUMBER,
    trueNumber: trueNumber,
});

export const updateFalseNumber = (falseNumber) => ({
    type: UPDATE_FALSE_NUMBER,
    falseNumber: falseNumber,
});

export const updateStatus = (status) => ({
    type: UPDATE_STATUS,
    status: status,
});

export const updateImage = (image) => ({
    type: UPDATE_IMAGE,
    image: image,
});
